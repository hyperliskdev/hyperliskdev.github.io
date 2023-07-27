---
layout: post
title:  "Understanding Resources"
date:   2023-07-24
categories: ics electrical power 
---


One of the most important aspects of being a good hacker is understanding the things you are trying to hack. At the same time, this is important for defenders of critical infrastructure. To protect any system, you need to know how the system works, how it can be compromised and how it can be defended. People devote their lives and work extremely hard on just one of these aspects, it can seem unrealistic to understand just one never mind all three. In this post, I want to start to outline how the electrical systems of Earth work. I am going into this with no training and no professional experience in any critical resources.


-- References --

[OSHA Electric Power](https://www.osha.gov/etools/electric-power/illustrated-glossary/distribution-system)



## Electrical Power



<img style="float: right; width: 50%;" src="/assets/img/osha-electrical-image.png">

To start, I want to get a basic understanding of all the aspects of how electrical distribution works. Since I am based in North America, I will be researching North American standards and particularly using OSHA's illustrated guide. 

At the beginning of the electrical grid, is the generation of electricity. The learning goals for generation are to understand the control points of the generators (places where PLC could exist) and how the power leaves the generators.

### Generation

First off, Thermal Power. The basic idea behind this is to burn fuel, create heat and then use the heat to spin a generator. 

Let's describe the fuel in some code;

```rust
// A trait that contains the most basic information about a fuel source.
trait Fuel {
    // Higher Heating Value - MJ/kg
    fn heating_value(&self) -> f64;
    // kJ/kg * C
    fn specific_heat(&self) -> f64;

    fn density(&self) -> f64;
}

trait Coal: Fuel {

    // Proximate Analysis
    fn fixed_coal(&self) -> f64;
    fn volatile_coal(&self) -> f64;
    fn ash_content(&self) -> f64;


    // Ultimate Analysis
    fn carbon(&self) -> f64;
    fn hydrogen(&self) -> f64;
    fn oxygen(&self) -> f64;
    fn nitrogen(&self) -> f64;
    fn sulfur(&self) -> f64

    fn water(&self) -> f64;
}
```