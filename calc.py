# calcu.py

def cal(account_balance, risk_amount, stop_loss, info, reward):
        risk = account_balance * risk_amount
        valor = info['valor_p']
        contracts = max(1, int(risk // (stop_loss * valor)))
        stop = stop_loss * valor * contracts
        outcome = contracts * reward * valor

        return {
            "balance total": f"${account_balance:.2f}",
            "riesgo en usd": f"${risk:.2f}",
            "valor por punto": f"${valor}",
            "contratos": contracts,
            "stop total (usd)": f"${stop:.2f}",
            "recompensa (usd)": f"${outcome:.2f}",
        }
def risk_contracts_calc(risk_usd, stop_loss, info):
    valor = info['valor_p']
    contracts = max(1, int(risk_usd // (stop_loss * valor)))
    stop_total = stop_loss * valor * contracts

    return {
        "riesgo total (usd)": f"${risk_usd:.2f}",
        "valor por punto": f"${valor}",
        "contratos sugeridos": contracts,
        "stop total (usd)": f"${stop_total:.2f}",
    }