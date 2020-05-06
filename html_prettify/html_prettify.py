# TODO: The html5lib and lxml parsers aren't working.
# import html5lib
# import lxml
from bs4 import BeautifulSoup
from grow import extensions
from grow.extensions import hooks
from grow.documents import document

class HtmlPrettifyPostRenderHook(hooks.PostRenderHook):

    def trigger(self, previous_result, doc, raw_content, *_args, **_kwargs):
        print raw_content

        # Execute post-render modification.
        if not isinstance(doc, document.Document) or not doc.view.endswith('.html'):
            return previous_result
        content = previous_result if previous_result else raw_content
        soup = BeautifulSoup(content, 'html.parser')
        # TODO: Issue with `html.parser` is that it converts html attributes without values to empty strings (i.e. <body devsite> --> <body devsite="">)
        # Possible workaround - would replace all attributes with empty string values into True values. This could be problematic however, if there was an attribute that
        # needed to be an empty string and not True.
        # for tag in soup:
        #     for attr in tag.attrs:
        #         if tag.attrs[attr] == "":
        #             tag.attrs[attr] = True

        return soup.prettify()


class HtmlPrettifyExtension(extensions.BaseExtension):

    @property
    def available_hooks(self):
        # Returns the available hook classes.
        return [HtmlPrettifyPostRenderHook]