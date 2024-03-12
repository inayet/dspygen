from pydantic import BaseModel, Field

from dspygen.modules.gen_pydantic_instance_module import GenPydanticInstance
from dspygen.utils.dspy_tools import init_dspy


class EventStormingDomainSpecificationModel(BaseModel):
    """Integrates Event Storming with RDDDY and DFLSS to capture and analyze domain complexities through events, commands,
    and queries, using Hoare logic for correctness. It serves as a repository for interactions identified in
    Event Storming, enhancing system responsiveness and process efficiency. This model educates on designing and
    verifying systems aligned with domain requirements and operational excellence. CamelCase only.
    """

    domain_event_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of domain event names triggering system reactions. Examples: 'OrderPlaced', 'PaymentProcessed', 'InventoryUpdated'.",
    )
    external_event_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of external event names that originate from outside the system but affect its behavior. Examples: 'WeatherChanged', 'ExternalSystemUpdated', 'RegulationAmended'.",
    )
    command_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of command names driving state transitions. Examples: 'CreateOrder', 'ProcessPayment', 'UpdateInventory'.",
    )
    query_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of query names for information retrieval without altering the system state. Examples: 'GetOrderDetails', 'ListAvailableProducts', 'CheckCustomerCredit'.",
    )
    aggregate_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of aggregate names, clusters of domain objects treated as a single unit. Examples: 'OrderAggregate', 'CustomerAggregate', 'ProductAggregate'.",
    )
    policy_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of policy names governing system behavior. Examples: 'OrderFulfillmentPolicy', 'ReturnPolicy', 'DiscountPolicy'.",
    )
    read_model_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of read model names optimized for querying. Examples: 'OrderSummaryReadModel', 'ProductCatalogReadModel', 'CustomerProfileReadModel'.",
    )
    view_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of view names representing user interface components. Examples: 'OrderDetailsView', 'ProductListView', 'CustomerDashboardView'.",
    )
    ui_event_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of UI event names triggered by user interactions. Examples: 'ButtonClick', 'FormSubmitted', 'PageLoaded'.",
    )
    saga_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of saga names representing long-running processes. Examples: 'OrderProcessingSaga', 'CustomerOnboardingSaga', 'InventoryRestockSaga'.",
    )
    integration_event_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of integration event names exchanged between different parts of a distributed system. Examples: 'OrderCreatedIntegrationEvent', 'PaymentConfirmedIntegrationEvent', 'InventoryCheckIntegrationEvent'.",
    )
    exception_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of exception names representing error conditions. Examples: 'OrderNotFoundException', 'PaymentFailedException', 'InventoryShortageException'.",
    )
    value_object_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of immutable value object names within the domain model. Examples: 'AddressValueObject', 'MoneyValueObject', 'QuantityValueObject'.",
    )
    task_classnames: list[str] = Field(
        ...,
        min_length=3,
        description="List of task names needed to complete a process or workflow. Examples: 'ValidateOrderTask', 'AllocateInventoryTask', 'NotifyCustomerTask'.",
    )



requirements = """The project must integrated the shippiing labels produced by USP ConnectShip shipping station with the certification number generated by the decision tree questionnaire.

At the time of the shipping lable being produced, the event should halt moving to the next screen of the lable pritning process and invoke the browser.  The browser loads order specific questionnariere described as a decision tree and allow technician t provide answers about the order being packaed.

Once the questionnaire is complete, the browser s closed, the questionnare cerificate id be posted and included to be printed to shipping label.

The decision tree selection is based on types of products in the order and should be managed / created by business analysts."""


def main():
    init_dspy(model="gpt-4")

    pred = GenPydanticInstance(root_model=EventStormingDomainSpecificationModel)

    model = pred(requirements)

    print(model)



if __name__ == '__main__':
    main()
