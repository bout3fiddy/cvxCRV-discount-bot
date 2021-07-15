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


def get_cvxCRV_discount_rate(sushiswap_router_contract):

    cvxCRV_contract = "0x62B9c7356A2Dc64a1969e19C23e4f579F9810Aa7"
    CRV_contract = "0xD533a949740bb3306d119CC777fa900bA034cd52"

    amounts_out = sushiswap_router_contract.functions.getAmountsOut(
        int(1000 * 1e18), [CRV_contract, cvxCRV_contract]
    ).call()

    discount_rate = 100 * (amounts_out[1] - amounts_out[0]) / amounts_out[0]

    return discount_rate


def main():
    print(get_cvxCRV_discount_rate())


if __name__ == "__main__":
    main()
