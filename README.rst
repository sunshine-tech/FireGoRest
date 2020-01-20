==========
FireGoRest
==========


Some utilties to work with Google Firestore API.

First utility is ``firegorest.tidy_doc``, to make a neat data dictionary from the `event`_ passed by Google Cloud runtime to your cloud function.

Install
-------

    pip install firegorest


Example
-------

.. code-block:: python

    from logbook import Logger
    from firegorest import tidy_doc
    from firegorest.types import GCFContext

    logger = Logger(__name__)


    def act_on_customer_change(event: dict, context: GCFContext):
        try:
            logger.info('Old Value: {}', tidy_doc(event['oldValue']['fields']))
        except KeyError:
            pass
        try:
            logger.info('New Value: {}', tidy_doc(event['value']['fields']))
        except KeyError:
            pass
        resource = context.resource
        logger.debug('Resource: {}', resource)
        return True



.. _event: https://cloud.google.com/functions/docs/calling/cloud-firestore#event_structure
