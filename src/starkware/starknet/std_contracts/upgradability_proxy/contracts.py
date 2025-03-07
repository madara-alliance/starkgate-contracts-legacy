import os.path

from starkware.starknet.services.api.contract_class.contract_class import DeprecatedCompiledClass

DIR = os.path.dirname(__file__)

proxy_contract_class = DeprecatedCompiledClass.loads(data=open(os.path.join(DIR, "proxy.json")).read())
governance_contract_class = DeprecatedCompiledClass.loads(
    data=open(os.path.join(DIR, "governance.json")).read()
)
