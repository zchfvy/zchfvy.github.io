Title: Hello World
Date: 2016-02-01 23:11
Modified: 2016-02-01 23:43
Category: Misc
Tags: pelican, aws, website
Slug: helloworld
Authors: Jason Hamilton-Smith
Summary: An introduction to my website, and how it was created.


Looks like I finally did it! I made a webpage! I'l probably be using this to
post about cute little code side-projects I work on mostly, but who knows where
time will take me. For now, a little article on how I set up the site itself.


How I made this Webpage
=======================


When I set out to make a website, I had two big requirements:

* It must not be permanently tied to some third-party service I cannot control.
* It must be easy to use.

Of course, the above two often conflict. Enter the awesome 'Pelican' tool:
with it I can have my site generated locally on my PC, out of source files
I create without any external service  requirements (And, of course, Pelican
is open source too!). I will never be prey to the service I am based on
shutting down or anything of that sort (I am posting this days after Parse
announced their shutdown).

On the other hand, I do need somewhere to host my code, and for that I chose
AWS. It **is** a service out of my control, but I am not tied to it, my site
is static HTML that lives on my own computer, and I can move it to theoreticaly
any hosting service.

That out of the way, here's how I set up this whole operation:


Tools
-----

First off, here's a listing of the tools I used for this:

* [pelican](http://blog.getpelican.com/)
* [alchemy theme](https://github.com/nairobilug/pelican-alchemy/tree/43f23f05b9adc0c6bf18d2f4ebd47771a7fe8f4a)
* [aws](http://aws.amazon.com)
* [letsencrypt](https://letsencrypt.org/)
* [this letsencrypt plugin](https://github.com/dlapiduz/letsencrypt-s3front)


Setting up Pelican with S3
--------------------------

This was very straightforward, I followed
[this](http://lexual.com/blog/setup-pelican-blog-on-s3/) guide and it worked
the first time. Though note, the `pelican-quickstart` command doesn't\*
appear to have defaults for every option, I didn't know what my domain was
going to be at the time, but it turns out changing these values after is super
easy, just look in the generated `pelicanconf.py` and `publishconf.py`.

I didn't actualy start making content pages (or rather, this content page)
until I had completed all the other steps and was happy with my setup, but
that was also straightforward. I am using Markdown as described
[here](http://docs.getpelican.com/en/3.6.3/quickstart.html).


Configuring the website
-----------------------

This step was just as straightforward as the first part, but more time
consuming, largely due to me guessing for myself what to do until just
deciding to follow Amazon's tutorial
[here](http://docs.aws.amazon.com/gettingstarted/latest/swh/website-hosting-intro.html).
I already made the buckets in the first step, and in retrospect may have done
this out of order. A big part of this step is waiting for DNS to propogate,
and waiting for Cloudfront to start up. I don't think I need the speed of a
CDN for such a small site, but Cloudfront is required to use HTTPS in this
setup, as desribed in the next step.


Setting Up Letsencrypt
----------------------

This part was not hard, but did require a bit of fiddling. I already had found
the afformentioned plugin when I started this step, so all there was to do was
use it. I copied the snippet from the readme into an `update_cert.sh` and
filled in my AWS credentials (I put this in a **seperate** folder from the main
website to avoid putting credentials in my git repository).

When I ran the script there were still a few issues first I had to update some
modules from pip, `pip install --upgrade letsencrypt` accomplished that easily.
Secondly, the AWS user that the credentials were tied too was setup wrong, a
bit of fiddling revealed it needs the following:

* Access to the S3 bucket the website is in
* Access to Cloudfront's configuration
* The following policy for uploading certificates:

```
    {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "iam:UploadServerCertificate"
              ],
              "Resource": "*"
          }
      ]
    }
```


Looking Forward
===============

While setting up this website took time, it wasn't all that hard for something
that is so custom. And actualy writing this content page was a breeze! In the
future I may look at some more pelican plugins (the IPython notebook one looks
primising). I'l probably also be adding some more general purpose pages in
addition to the blog. I also *might* look at running a Flask server on an AWS
micro instance if I have the need for a small dynamic server.

All said, I'm glad I finally got around to making this, now to work on some
real content!
