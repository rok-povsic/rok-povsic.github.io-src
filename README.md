## Blog source for rokpovsic.com

### Useful blog resources:
- [How to setup Pelican for GitHub](https://fedoramagazine.org/make-github-pages-blog-with-pelican/)
- [Setting up https for custom domains](https://sheharyar.me/blog/free-ssl-for-github-pages-with-custom-domains/)

### Build & publish
Build the output HTML:

    pelican content/ -o output/ -s pelicanconf.py

Run dev server:

    cd output && python -m pelican.server 8080

Publish by committing & pushing.
