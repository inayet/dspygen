"""

"""
import dspy

from dspygen.utils.dspy_tools import init_dspy


class BusinessRequirementsSignature(dspy.Signature):
    """Transforms business requirement descriptions provided in BPMN format into DMN YAML format."""

    bpmn = dspy.InputField(desc="Business Process Model and Notation as input")

    dmn_yaml = dspy.OutputField(
        desc="Decision Model and Notation in YAML format as output", prefix="```yaml"
    )


class BusinessRequirementsModule(dspy.Module):
    """BusinessRequirementsModule"""

    def forward(self, bpmn):
        pred = dspy.ChainOfThought(BusinessRequirementsSignature)
        result = pred(bpmn=bpmn).dmn_yaml
        return result


from typer import Typer

app = Typer()


@app.command()
def call(bpmn):
    """BusinessRequirementsModule"""
    init_dspy()

    print(business_requirements_call(bpmn=bpmn))


def business_requirements_call(bpmn):
    business_requirements = BusinessRequirementsModule()
    return business_requirements.forward(bpmn=bpmn)


bpmn = """The project must integrated the shippiing labels produced by USP ConnectShip shipping station with the certification number generated by the decision tree questionnaire.

At the time of the shipping lable being produced, the event should halt moving to the next screen of the lable pritning process and invoke the browser.  The browser loads order specific questionnariere described as a decision tree and allow technician t provide answers about the order being packaed.

Once the questionnaire is complete, the browser s closed, the questionnare cerificate id be posted and included to be printed to shipping label.

The decision tree selection is based on types of products in the order and should be managed / created by business analysts."""


def main():
    init_dspy()
    print(business_requirements_call(bpmn=bpmn))


from fastapi import APIRouter

router = APIRouter()


@router.post("/business_requirements/")
async def business_requirements_route(data: dict):
    # Your code generation logic here
    init_dspy()

    print(data)
    return business_requirements_call(**data)


"""
import streamlit as st


# Streamlit form and display
st.title("BusinessRequirementsModule Generator")
bpmn = st.text_input("Enter bpmn")

if st.button("Submit BusinessRequirementsModule"):
    init_dspy()

    result = business_requirements_call(bpmn=bpmn)
    st.write(result)
"""

if __name__ == "__main__":
    main()
