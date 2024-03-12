from dspygen.rdddy.abstract_actor import AbstractActor


class AbstractSaga(AbstractActor):
    """Encapsulates the logic for managing long-running, complex business transactions that span multiple services or
    bounded contexts. It provides mechanisms for orchestrating sequences of domain events and commands,
    ensuring transactional consistency and compensating actions in case of failures. By extending AbstractSaga,
    developers can implement coordinated workflows that are robust and aligned with business processes.
    """

