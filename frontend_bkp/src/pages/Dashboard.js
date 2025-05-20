import React, { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
  const [dados, setDados] = useState([]);
  const [metricas, setMetricas] = useState({});
  const [rondonia, setRondonia] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/dados").then((res) => setDados(res.data));
    axios.get("http://localhost:8000/metricas").then((res) => setMetricas(res.data));
    axios.get("http://localhost:8000/rondonia").then((res) => setRondonia(res.data));
  }, []);

  return (
    <div style={{ padding: 24 }}>
      <h1>Análise de Renda - PNAD 2023</h1>

      <section>
        <h2>📈 Métricas dos Modelos</h2>
        {Object.entries(metricas).map(([modelo, metrica]) => (
          <div key={modelo}>
            <h3>{modelo}</h3>
            <pre>{JSON.stringify(metrica, null, 2)}</pre>
            <img
              src={`/static/grafico_real_predito_${modelo}.png`}
              alt={modelo}
              style={{ maxWidth: "500px" }}
            />
          </div>
        ))}
      </section>

      <section>
        <h2>🔎 Estatísticas de Rondônia</h2>
        <table border="1">
          <thead>
            <tr>
              {rondonia[0] &&
                Object.keys(rondonia[0]).map((key) => <th key={key}>{key}</th>)}
            </tr>
          </thead>
          <tbody>
            {rondonia.map((row, idx) => (
              <tr key={idx}>
                {Object.values(row).map((val, j) => (
                  <td key={j}>{val}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}

export default Dashboard;