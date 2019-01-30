Title: The wonders of certbot
Date: 2019-01-29 22:56
Modified: 2019-01-29 22:56
Category: Misc
Tags: aws, website, certbot
Slug: certbot
Authors: Jason Hamilton-Smith
Summary: Dealing with reinstalling certbot, AKA I have no idea what I'm doing.


Through the past three years, despite me not updating this blog, I did keep
updating the site's certificate just to keep it running. A couple months back I
suffered a hard drive failure, and now that the certificate is expiring again I
was faced with the prospect of re-installing certbot.

For me, at least, certbot/letsencrypt has been a constant battle. Every 3 months
I need to remember the arcane sequence of commands, which virtualenvs I had
things installed in, and the like. But for the most part a series of scripts
kept it manageable. But reinstalling certbot, along with the plugin I needed to
use, was another ordeal entirely.

The first issue was that certbot is currently designed to run on the same
web-server that it is providing certificates for, which is not an option with a
site hosted on an S3 bucket like mine. The alternative was a tool called
'certbot-auto' available
[here](https://certbot.eff.org/docs/install.html#installing-from-source) that
behaved... kind-of like the old certbot.  Finding out how to install it (3
options, the link above, with apt, or with pip) took a fair bit of
experimenting, and then where to install it (virtualenv) took a fair bit more;
and that goes double for the plugin 'certbot-s3front' mentioned in my first blog
post.

At the end, it turns out the linked utility should be run directly, and the
plugin then needs to be installed in a special virtualenv located in
/opt/eff.org/certbot/venv, owned by root. So I needed to first run the following

```
sudo -i
source /opt/eff.org/certbot/venv/bin/activate
pip install certbot-s3front
```

And only then did things work as described in my first post.


Well... nearly. It turns out that in addition to doing things in a special
virtualenv certbot-auto also does things with a "fresh" set of environment
variables, so passing the AWS credentials via environment no-longer works. After
fighting this too for a while I realized there was no simple solution, the
plugin itself would need a new version to address this issue.

[So I made a new version.](https://github.com/zchfvy/certbot-s3front)

And with that installed things finally worked... until N eed to update the certs
again.

I also made a pull request to get merged it into the main repository, I don't
fully know if it's necessary because I don't know if everything I did here is
wrong anyways. Right now it's held up because it's failed on a Microsoft...
thing, and also needs the approval of the maintainer of-course, but if that gets
merged I'll update the article. Until then, here's to another 3 years!
