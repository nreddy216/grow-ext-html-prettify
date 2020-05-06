# grow-ext-html-prettify

Simple extension for prettifying html after Grow renders a page.

## Usage

### Initial setup

1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/grow/grow-ext-html-min`
1. Run `grow install`.
1. Add the following section to `podspec.yaml`:

```
ext:
- extensions.html_min.HtmlPrettifyExtension
```

When rendering HTML pages Grow will prettify the resulting html.

<!-- ### Options

The configuration can also be used with the options for [`htmlmin`](https://htmlmin.readthedocs.io/en/latest/reference.html#htmlmin.minify).

For example:

```
ext:
- extensions.html_min.HtmlMinExtension:
    options:
      remove_comments: true
      reduce_boolean_attributes: false
``` -->
