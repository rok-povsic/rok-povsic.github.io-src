Title: Setting up a static-site blog from scratch
Date: 2018-12-15 19:08
Category: blog, pelican, isso
Tags: blog, pelican, isso
Authors: Rok Povšič

This blog is built with a static-site generator named [Pelican](https://blog.getpelican.com/). It converts the posts you write in Markdown directly to HTML files, which happens on your machine at "compile-time". This means there's no dynamic page generation on each HTTP request, which is fine (even preferred) for a blog-like website (though I'll explain how to setup a commenting system). Pelican is written in Python and using it *feels Pythonic* (it uses configuration-as-code) which is great for any hardcore Pythonista.

<!-- PELICAN_END_SUMMARY -->

Pelican is very flexible allowing you to modify the blog to your needs. [A number of quality plugins](https://github.com/getpelican/pelican-plugins) exist, of which I currently use **summery**, allowing me to specify the exact text shown on the index page under post summary, and **yuicompressor**, which at compile-time, minifies all CSS and JS files.

There exists a number of [Pelican themes](https://github.com/getpelican/pelican-themes). I'm using the [Clean Blog theme](https://github.com/gilsondev/pelican-clean-blog) which I've modified slightly. It's clean and simple, and hopefully won't end up looking outdated in a couple of years.

The blog is hosted on [GitHub Pages](https://pages.github.com/) which is tightly integrated with the GitHub repository hosting the HTML files, allowing the deployment of the files to happen solely using git (`git push` and that's it). The process of writing and publishing a new post is simple. Write the post, compile the HTML files, push to the GitHub repository. [Make a Github Pages blog with Pelican](https://fedoramagazine.org/make-github-pages-blog-with-pelican/) is the tutorial I've followed to set this up.

At this point I setup my own domain name. I've registered it at [GoDaddy](https://uk.godaddy.com/) and then followed the [Set Up SSL on Github Pages With Custom Domains for Free](https://sheharyar.me/blog/free-ssl-for-github-pages-with-custom-domains/) tutorial which uses Cloudflare to make the domain work using *https*.

Recently, I've also setup the commenting system. A usual choice of the platform would be [Disqus](https://disqus.com) but wanted find an alternative because of privacy concerns. Personally, I also don't find its looks attractive. I've instead chosen [Isso](https://posativ.org/isso/) which I self-host with one of the cloud providers.

Isso integration to Pelican is quite simple but takes time. Client-side there are only couple if lines of code you add to your Pelican them. Server-side, you have to setup an Nginx reverse-proxy which sends requests to your Isso instance, setup some kind of Certificate Authority (in my case [Let's Encrypt](https://letsencrypt.org/)) so you don't send user's comments over the wire unencrypted, and a SMTP send-mail server if you want to your commentators to be notified of replies via mail.

All in all, this takes more time to setup than using some out-of-the-box solution (i.e. Wordpress). But the process was quite fun and the end result is quite good.