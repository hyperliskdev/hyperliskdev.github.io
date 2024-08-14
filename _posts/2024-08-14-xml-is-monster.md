---
layout: post
title: "What the hell is going on with Excel Files"
date: 2024-08-14
categories: github programming project
---

Hello!

I've been working on an NDA project for a company called Indiva, which produces a significant portion of the edibles consumed in Canada. A large part of my job involves writing to Excel files using code. The challenge is that some libraries for the restricted languages I can use are either incomplete or lack the functionality I need.

### Part I: Problem Identification

This led me to make some modifications to a library called ExcelJS, notably disabling the AutoFilter read/render feature. This brings us to the main topic of this post. When using the default version of ExcelJS, why did the Excel Web client show this error when I wrote data to a file in SharePoint using TypeScript? ![alt text](/assets/img/xml-is-monster/xlsx-error.png)

To investigate, I conducted basic tests on different ways ExcelJS can read/write data.

1. `workbook.xlsx.load(buffer)`

   - Initially, I thought ExcelJS had its own Buffer type. However, it turns out ExcelJS.Buffer is just a browser wrapper around the standard Buffer type.

2. `workbook.xlsx.read(stream)`
   - The library used to read data from SharePoint doesn't read file contents as a stream. I tried converting a buffer into a stream, but it yielded the same results.

After these tests, I made an observation that led to the real answer.

![alt text](/assets/img/xml-is-monster/image.png)

Considering that ExcelJS might be the problem, I checked if others had encountered this issue. Indeed, several people had, as seen in these links: [[1]](https://github.com/exceljs/exceljs/issues/2184) [[2]](https://github.com/exceljs/exceljs/issues/400) [[3]](https://stackoverflow.com/questions/70780976/xlsx-error-removed-records-document-theme-from-xl-workbook-xml-part-workboo). I decided to examine the Excel file before and after making changes to see what was breaking it.

Things got more complex here. Excel files are essentially zip files containing multiple XML files that store the document's data, properties, and information from the 'provider/consumer' of the file.

The XML Schema Definition is a library for XML that allows users to use a defined set of elements in a specific XML file. So, we have multiple XML files using a set of defined schemas.

Let's find the section where an autofilter is created in the malformed Excel file.

```xml
<!--
     Broken excel file autofilter section
-->
<autoFilter ref="A1:B5">
     <filterColumn colId="0" hiddenButton="1"/>
     <filterColumn colId="1" hiddenButton="1"/>
</autoFilter>
```

This makes sense; there's an autofilter on the area from A1:B5 with two columns having hiddenButton attributes. Now, let's look at a working Excel file with an autofilter...

```xml
<!--
     Working excel file autofilter section
-->
<autoFilter ref="A1:B5" xr:uid="{UUID}">
     <filterColumn colId="0">
          <filters>
                <filter val="">
                <filter val="">
                <filter val="">
          </filters>
     </filterColumn>
</autoFilter>
```

Clearly, they're different, and Excel doesn't like that. So, how can we fix this? Unfortunately, the answer lies in reading the largest document on my computer at the moment.

### Part II: Office Open XML Standard

Okay, so I haven't read a ton of standardization documents. Actually, only one other before on Kerberos authentication, it wasn't something I was itching to do again.

ISO/IEC 29500 or ECMA-376 are the two standard names for Office Open XML. There is a set of 4 documents outlining how three main document types (.xlsx, .pptx and .docx) are structured.

So, we know we need to look at this `<autoFilter>` tag and find out if something if different even further.

![alt text](/assets/img/xml-is-monster/autoFilter.png)

This photo shows that there is another tag called `customFilters` and `customFilter` but on the working example above these two are structurally the same. If we look a little further, there is a section (18.3.2) all about how autoFilters work in the XML.

![](/assets/img/xml-is-monster/filters.png)

Plus the array identifier element `filters` plural.

Something is wrong with how ExcelJS reads the file and then renders the resulting object.

Since, I didnt specifically need the autofilter to be changed, I dont need the library to even read that section. So, I decided to write a fix and take a look at the code that performs these actions and sure enough, it is incorrect.

This is the render method on the class which is an analogue for the filterColumn element. (FilterColumnXForm)

It checks if the provided model contains customFilters and performs the rendering of inner custom filter tags.
AutoFilterXForm
Then instead of following the same logic and creating an open `filters` node then rendering those internal leafNode, the leafNode is rendered as filterColumn (`this.tag = 'filterColumn'`).

```javascript
// filter-column-xform.js render method

// --- snip

render(xmlStream, model) {
    if (model.customFilters) {
        xmlStream.openNode(this.tag, {
        colId: model.colId,
        hiddenButton: model.filterButton ? '0' : '1',
        });

        this.map.customFilters.render(xmlStream, model.customFilters);

        xmlStream.closeNode();
        return true;
    }
    xmlStream.leafNode(this.tag, {
        colId: model.colId,
        hiddenButton: model.filterButton ? '0' : '1',
    });

    return true;
}

// --- snip
```

The fix is easy and just adding an if statement and rendering the filters just like customFilters is rendered.

```javascript

// filter-column-xform.js new render method

// --- snip

constructor() {
    super();

    this.map = {
      customFilters: new ListXform({
        tag: 'customFilters',
        count: false,
        empty: true,
        childXform: new CustomFilterXform(),
      }),
      filters: new ListXform({
        tag: 'filters',
        count: false,
        empty: true,
        childXform: new FilterXform(),
      }),
    };
  }


// --- snip

render(xmlStream, model) {
    if (model.customFilters) {
      xmlStream.openNode(this.tag, {
        colId: model.colId,
        hiddenButton: model.filterButton ? '0' : '1',
      });

      this.map.customFilters.render(xmlStream, model.customFilters);

      xmlStream.closeNode();
      return true;
    }
    if (model.filters) {
      xmlStream.leafNode(this.tag, {
        colId: model.colId,
        hiddenButton: model.filterButton ? '0' : '1',
      });

      this.map.filters.render(xmlStream, model.filters);

      xmlStream.closeNode();
      return true;

    }
  }

// --- snip
```


Thats the basics of this problem. It seems like there are several other of these issues with ExcelJS but I don't blame the owner/maintainer. To manage something like this completely free and also all the tiny working intricacies.


If you made it to the end, thank you for reading and the main purpose of this post is to tell you that I have made an attempt at working with OOXML in specifically Typescript because thats what I was using.

This one is a little bigger than ExcelJS as I want to support reading and writing to parts of all three documents outlined in ISO/IEC 29500 & ECMA-376. (.pptx, .docx and .xlsx)

I think that some of the development techniques and structures from ExcelJS will work quite well for this as well.

Here is a link to the [project](https://github.com/hyperliskdev/ooxml-ts) and a [link](https://www.npmjs.com/package/@hyperliskdev/exceljs?activeTab=readme) to the autofilter fix for ExcelJS if you are also having problems with it.