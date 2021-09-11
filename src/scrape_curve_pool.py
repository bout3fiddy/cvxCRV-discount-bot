import os

import web3
from etherscan.contracts import Contract as EtherscanContract


w3_infura = web3.Web3(
    web3.Web3.HTTPProvider(
        f"https://mainnet.infura.io/v3/{os.environ['WEB3_INFURA_PROJECT_ID']}",
    ),
)


def init_contract(address: str):

    address = web3.Web3.toChecksumAddress(address)
    contract_abi = EtherscanContract(
        address=address,
        api_key=os.environ["ETHERSCAN_API_KEY"],
    ).get_abi()
    contract = w3_infura.eth.contract(address=address, abi=contract_abi)
    return contract


def get_cvxCRV_discount_rate(pool_contract, crv_in: int = 1e22):

    cvxcrv_out = pool_contract.functions.get_dy(
        0, 1, int(crv_in)
    ).call()

    discount_rate = 100 * (cvxcrv_out - crv_in) / cvxcrv_out

    return discount_rate


def main():

    curve_cvxcrv_factory_pool = init_contract(
        "0x9D0464996170c6B9e75eED71c68B99dDEDf279e8"
    )

    print(get_cvxCRV_discount_rate(curve_cvxcrv_factory_pool))


if __name__ == "__main__":
    main()
