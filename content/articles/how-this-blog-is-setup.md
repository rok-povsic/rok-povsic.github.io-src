Title: Setting up a static-site blog on GitHub pages on a custom domain, with comments
Date: 2018-12-30 11:05
Category: blog, pelican, isso
Tags: blog, pelican, isso
Authors: Rok Povšič

This blog is built using a static-site generator named [Pelican](https://blog.getpelican.com/). It converts the posts you write in Markdown directly to HTML files, which happens on your machine at "compile-time". This means there's no dynamic page generation on each HTTP request, which is fine (even preferred) for a blog-like website. Pelican is written in Python and using it *feels Pythonic* (it uses configuration-as-code) which is great for any hardcore Pythonista. I've just recently also added a commenting system and will explain here what the blog's components are.

<!-- PELICAN_END_SUMMARY -->

Pelican is very flexible allowing you to modify the blog to your needs. [A number of quality plugins](https://github.com/getpelican/pelican-plugins) exist, of which I currently use **summery**, allowing me to specify the exact text shown on the index page under post summary, and **yuicompressor**, which at compile-time, minifies all CSS and JS files.

There exist a number of [Pelican themes](https://github.com/getpelican/pelican-themes). I'm using the [Clean Blog theme](https://github.com/gilsondev/pelican-clean-blog) which I've slightly modified. It's clean and simple, and hopefully won't end up looking outdated in a couple of years.

The blog is hosted on [GitHub Pages](https://pages.github.com/) which is tightly integrated with the GitHub repository hosting the HTML files, allowing the deployment of the files solely using Git (`git push` and that's it). The process of writing and publishing a new post is simple. Write the post, compile the HTML files, push them to the GitHub repository. [Make a Github Pages blog with Pelican](https://fedoramagazine.org/make-github-pages-blog-with-pelican/) is the tutorial I've followed to set this up.

I've also setup my own domain name. I've registered it at [GoDaddy](https://uk.godaddy.com/) and then followed the [Set Up SSL on Github Pages With Custom Domains for Free](https://sheharyar.me/blog/free-ssl-for-github-pages-with-custom-domains/) tutorial which uses Cloudflare to setup *https*.

Recently, I've also added the commenting system. A usual choice of the platform would be [Disqus](https://disqus.com) but I wanted find an alternative because of privacy concerns. Personally, I also don't find looks of Disqus attractive. I've instead chosen [Isso](https://posativ.org/isso/) which I self-host with one of the cloud providers.

Isso integration to Pelican is quite simple but takes time to set everything up. Client-side, you only add a couple of lines of HTML/JavaScript code to your Pelican theme. Server-side, you have to setup an Nginx reverse-proxy which sends requests to your Isso application (I run it inside of a Docker container), setup some kind of Certificate Authority (in my case [Let's Encrypt](https://letsencrypt.org/)) so you don't send user's comments over the wire unencrypted, and a SMTP send-mail server if you want to your commentators to be notified of replies via email.

All in all, this takes more time to setup than using some out-of-the-box solution (i.e. Wordpress). But the process was quite fun and at the end, the blog is more customizable, privacy-conscious, and efficient.
