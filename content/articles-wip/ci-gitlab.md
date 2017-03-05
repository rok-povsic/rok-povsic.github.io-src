Title: A complete continuous integration guide for .NET with GitLab CI
Date: 2017-03-04 8:30
Category: continuous-integration, gitlab, .net
Tags: continuous-integration, gitlab, .net
Authors: Rok Povšič

Here, I describe the process of setting up [continuous integration (CI)](https://en.wikipedia.org/wiki/Continuous_integration) for a C# project on [GitLab](https://gitlab.com). GitLab is a code sharing platform similar to GitHub but has two distinct advantages:
- you can create private repositories for free,
- it includes a free continuous integration tool called [GitLab CI](https://about.gitlab.com/gitlab-ci/) that can be run either on GitLab CI servers, or on your own server.

The free GitLab CI servers include only Linux machines at the time of this writing, so in this guide we are going to use our own Windows server to perform the actual builds and tests on. This means that to follow this guide, you **have to have a Windows instance for building the code**. This is ideally a computer that runs 24/7, i.e. a computer on premises or a VPS, but can also be your own computer for starters.

The continuous integration process will be the following:
1. You commit & push a set of code changes to a GitLab repository.
2. Next, your code is immediately automatically pulled from the repository to the Windows instance.
3. The C# compiler tries to build the code.
4. Unit tests/integration tests are run.
5. Badges are updated with the status.

In the end, you get a report of everything that happened, together with a badge like this (if the build was successful):
![A Success Build Badge]({filename}/images/ci-gitlab/success-badge.png)

To do this, let's create a test project in Visual Studio. We are going to do the build first and add automatic testing later.

This is the code:
