# generated by datamodel-codegen:
#   filename:  tezToTokenPayment.json

from __future__ import annotations

from pydantic import BaseModel, Extra


class TezToTokenPaymentParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    min_out: str
    receiver: str
