""" Basic callback definition. """

from sklearn.base import BaseEstimator


__all__ = ['Callback']


class Callback:
    """Base class for callbacks.

    All custom callbacks should inherit from this class. The subclass
    may override any of the ``on_...`` methods. It is, however, not
    necessary to override all of them, since it's okay if they don't
    have any effect.

    Classes that inherit from this also gain the ``get_params`` and
    ``set_params`` method.

    """
    def initialize(self):
        """(Re-)Set the initial state of the callback. Use this
        e.g. if the callback tracks some state that should be reset
        when the model is re-initialized.

        This method should return self.

        """
        return self

    def on_train_begin(self, net, **kwargs):
        """Called at the beginning of training."""
        pass

    def on_train_end(self, net, **kwargs):
        """Called at the end of training."""
        pass

    def on_epoch_begin(self, net, **kwargs):
        """Called at the beginning of each epoch."""
        pass

    def on_epoch_end(self, net, **kwargs):
        """Called at the end of each epoch."""
        pass

    def on_batch_begin(self, net, **kwargs):
        """Called at the beginning of each batch."""
        pass

    def on_batch_end(self, net, **kwargs):
        """Called at the end of each batch."""
        pass

    def on_grad_computed(self, net, named_parameters, **kwargs):
        """Called once per batch after gradients have been computed but before
        an update step was performed.

        """
        pass

    def _get_param_names(self):
        return (key for key in self.__dict__ if not key.endswith('_'))

    def get_params(self, deep=True):
        return BaseEstimator.get_params(self, deep=deep)

    def set_params(self, **params):
        BaseEstimator.set_params(self, **params)
