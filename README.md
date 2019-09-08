## Blog source for rokpovsic.com

### Useful blog resources:
- [How to setup Pelican for GitHub](https://fedoramagazine.org/make-github-pages-blog-with-pelican/)
- [Setting up https for custom domains](https://sheharyar.me/blog/free-ssl-for-github-pages-with-custom-domains/)

### Build & publish
Build the output HTML:

    make html

Run the dev server, runs at http://localhost:8000/ :

    make devserver
    make stopserver

Publish by committing & pushing inside of output/. Also commit & push source code in /.
