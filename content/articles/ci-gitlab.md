Title: A continuous integration guide for .NET with GitLab CI
Date: 2017-05-24 18:06
Category: continuous-integration, gitlab, .net
Tags: continuous-integration, gitlab, .net
Authors: Rok Povšič

Here, I describe the process of setting up [continuous integration (CI)](https://en.wikipedia.org/wiki/Continuous_integration) for a C# project that is hosted on [GitLab](https://gitlab.com). GitLab is a code sharing platform similar to GitHub but has two distinct advantages:

- you can create private repositories for free,
- it includes a free continuous integration tool called [GitLab CI](https://about.gitlab.com/gitlab-ci/) that can be run either on GitLab CI servers, or on your own server.

Actually, GitLab even provides their CI servers for free, called Shared Runners, but at the time of this writing only Linux servers are available, so in this guide we are going to use our own Windows server to perform the actual builds and tests on. This means that to follow this guide, you **have to have a Windows instance available** in order to run a build. For a production use this is ideally a computer that runs 24/7, i.e. a computer on premises or a VPS, but can, for starters, also be your own laptop/pc.

The continuous integration process we will do will be the following:

1. You commit & push a set of code changes to a GitLab repository.
2. Your code is immediately automatically pulled from the GitLab repository to the Windows instance.
3. The C# compiler tries to build the code.
4. Badges are updated with the status.

In the end, you get a report of everything that happened, together with a badge like this (if the build was successful):

![A Success Build Badge]({filename}/images/ci-gitlab/success-badge.png)

To do this, let's create a test project in Visual Studio. We are going to do the build first and add automatic testing later.

This is the sample code we are going to build:

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }

Create a new repository on GitLab. Next, install GitLab Runner, which is a program that runs on your Windows machine that is connected to the repository and that runs the build. Download the program from [here](https://docs.gitlab.com/runner/install/windows.html) where you will also find more details on how to install it. It's not complicated, but the one thing you'll also need is a *token* with which you connect Runner with the repository. You find it by opening your repository, and going to *Settings* -> *CI/CD Pipelines*. Copy the token and follow the instructions on how to install and connect the runner.

Note: If you only want to build this project on your server, click *Disable Shared Runners* so GitLab won't try to build this project on their servers.

After this, the next step is to configure how exactly the build should be performed. This is done by creating a `.gitlab-ci.yml` file in the root of the project directory and specifying how to do the build. Here's a simple example:

    build:
        stage: build
        script:
                - C:\Tools\nuget.exe restore
                - cmd.exe /C " "C:\Program Files (x86)\MSBuild\14.0\Bin\MSBuild.exe" /p:Configuration=Release /t:Clean;Build YourSolutionName.sln " && exit %%ERRORLEVEL%%

You have to specify your location of `nuget.exe` and `MSBuild.exe`, and the solution name. You may download `nuget.exe` from [here](http://dist.nuget.org/). See [this StackOverflow page](https://stackoverflow.com/questions/42696948/how-can-i-install-the-vs2017-version-of-msbuild-on-a-build-server-without-instal) to find out how to get `MSBuild.exe`.

After that, every time a code is pushed on the repository, it will be automatically downloaded to the Windows machine that is running GitLab Runner. The build status will be reported under *Pipelines*.

![GitLab Pipelines]({filename}/images/ci-gitlab/ci-pipelines.png)

Next, you can show the latest build status on the main repository page by copying a Markdown badge code, located under *Settings* -> *CI/CD Pipelines*

![A Success Build Badge]({filename}/images/ci-gitlab/success-badge.png)
