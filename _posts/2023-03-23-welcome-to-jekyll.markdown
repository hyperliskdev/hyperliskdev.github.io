---
layout: post
title:  "Github Actions with pSQL and GraphQL: Part 1"
date:   2023-05-21
categories: github actions ci warehouse
thumbnail-img: /assets/img/gql.png
---

To get started with some production concepts, I am going to setup a large ci operation for warehouse. This will contain jobs for ensure migrations are working, each of the services builds, all of the graphQL querys are consistent with what the api documenetaiton says and it interacts with other parts correctly etc...

With so many different individual parts, create CI might be difficult given that I can't run a consistent postgreSQL instance. (at least I couldnt find a way to for all of the jobs and yml files in github, so I leave that for a future dev environment project...) Each of the sections of warehouse will have its own jobs and testing space.


For migrations, since they exist separate from all of the services, I can migrate them using a separate tool.


