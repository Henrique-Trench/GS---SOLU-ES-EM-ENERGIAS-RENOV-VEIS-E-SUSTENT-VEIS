import pandas as pd
import numpy as np
data = {
    'Hora': range(8, 18),
    'Consumo_Observado_kWh': [
        15.5,
        25.0,
        24.5,
        24.0,
        23.5,
        22.0,
        24.8,
        25.2,
        24.1,
        18.0
    ]
}

df = pd.DataFrame(data)

df.loc[df['Hora'] == 13, 'Desperdicio_Percentual'] = 0.20
df.loc[df['Hora'] == 17, 'Desperdicio_Percentual'] = 0.40
df['Desperdicio_Percentual'] = df['Desperdicio_Percentual'].fillna(0)

df['Consumo_Otimizado_kWh'] = df['Consumo_Observado_kWh'] * (1 - df['Desperdicio_Percentual'])

df['Desperdicio_kWh'] = df['Consumo_Observado_kWh'] - df['Consumo_Otimizado_kWh']

print("--- Análise de Consumo Energético Diário (kWh) ---")
print(df[['Hora', 'Consumo_Observado_kWh', 'Desperdicio_kWh', 'Consumo_Otimizado_kWh']])
print("\n" + "-"*50 + "\n")


total_desperdicio_diario = df['Desperdicio_kWh'].sum()
consumo_anual_observado = df['Consumo_Observado_kWh'].sum() * 250
consumo_anual_otimizado = df['Consumo_Otimizado_kWh'].sum() * 250

PRECO_KWH = 0.85
FATOR_CO2_POR_KWH = 0.45

economia_anual_reais = total_desperdicio_diario * 250 * PRECO_KWH

reducao_co2_anual_kg = total_desperdicio_diario * 250 * FATOR_CO2_POR_KWH


print(f"## 💡 Resultados da Análise de Desperdício e Otimização\n")

print(f"**Total de Desperdício Identificado (por dia):** {total_desperdicio_diario:.2f} kWh")
print(f"**Consumo Anual Observado (Estimado):** {consumo_anual_observado:.2f} kWh")
print(f"**Consumo Anual Otimizado (Estimado):** {consumo_anual_otimizado:.2f} kWh")
print("-" * 50)

print(f"**PROPOSTA DE AJUSTE:** Implementar **automação inteligente** (sensores/timers) para desligar luzes e equipamentos na hora do almoço e no fim do expediente, eliminando o desperdício de {total_desperdicio_diario:.2f} kWh/dia.")
print("-" * 50)

print(f"### 💰 Ganhos Econômicos Anuais Estimados")
print(f"A economia anual na conta de luz é de aproximadamente: **R$ {economia_anual_reais:.2f}**")

print(f"### 🌳 Ganhos Ambientais Anuais Estimados")
print(f"A redução anual de emissões de CO2 é de aproximadamente: **{reducao_co2_anual_kg:.2f} kg de CO2**")
print(f"(Isso equivale a uma redução de {reducao_co2_anual_kg / 150:.2f} viagens de carro de 100km, por exemplo.)")