import os.path

from starkware.starknet.services.api.contract_class.contract_class import DeprecatedCompiledClass

DIR = os.path.dirname(__file__)

erc20_contract_class = DeprecatedCompiledClass.loads(data=open(os.path.join(DIR, "ERC20.json")).read())
