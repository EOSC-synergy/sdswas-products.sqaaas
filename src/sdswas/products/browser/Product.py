from plone.dexterity.browser.view import DefaultView
from plone.app.contenttypes.browser.folder import FolderView
from plone import api
from plone.app.relationfield.behavior import IRelatedItems
from Acquisition import aq_parent
from sdswas.customViews.browser.NewsletterForm import NewsletterForm
import logging
class Product(FolderView):

    def update(self):
        ## Disable all portlets
        super(DefaultView, self).update()
        self.request.set('disable_plone.rightcolumn',1)
        self.request.set('disable_plone.leftcolumn',1)

    def get_products(self):

        brains = self.context.portal_catalog(
            portal_type=["product"],
            review_state="published",
            sort_on=["effective"])

        #brains = self.context.getFolderContents(contentFilter={"portal_type" : "presentation"})
        results = []
        for brain in brains:
            resObj = brain.getObject()
            results.append({
            'title': resObj.Title(),
            'description': resObj.Description(),
            'absolute_url': resObj.absolute_url(),
            })

        return results

    def related_items(self):

        logging.getLogger("sdswas.products.browser.Product").warning(
                       "Searching related products")

        products_folder = api.portal.get().unrestrictedTraverse("products")

        brains = self.context.portal_catalog(
            path = {
                'query': products_folder.absolute_url_path()},
            portal_type=["product"],
            review_state="published",
            sort_on=["effective"])

        #brains = self.context.getFolderContents(contentFilter={"portal_type" : "presentation"})
        results = []
        for brain in brains:
            resObj = brain.getObject()

            if resObj != self.context:
                logging.getLogger("sdswas.products.browser.Product").warning(
                    "product added to the list of related products: " +resObj.Title())

                results.append({
                'title': resObj.Title(),
                'description': resObj.Description(),
                'absolute_url': resObj.absolute_url(),
                })
            else:
                logging.getLogger("sdswas.products.browser.Product").warning(
                       "product NOT added to the list of related products: " +resObj.Title())


        return results

    def subscribe_link(self):
       return NewsletterForm.subscribe_link(self)