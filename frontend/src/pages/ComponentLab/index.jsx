import React from "react";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import Box from "@mui/material/Box";
import Divider from "@mui/material/Divider";
import VuiTypography from "components/VuiTypography";
import AlertSample from "./samples/AlertSample";

// ⬇️ Wrapper para seções nomeadas de testes
const Section = ({ title, children }) => (
  <Card sx={{ p: 3, mb: 4 }}>
    <VuiTypography variant="h6" gutterBottom>
      {title}
    </VuiTypography>
    <Divider sx={{ mb: 2 }} />
    {children}
  </Card>
);

// 💎 Página principal do laboratório
const ComponentLab = () => {
  return (
    <Box p={3}>
      <VuiTypography variant="h4" mb={4}>
        🔬 Component Lab
      </VuiTypography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Section title="🧪 VuiAlert (alertas)">
            <AlertSample />
          </Section>
        </Grid>

        {/* 🧩 Adicione novos testes de componentes assim: */}
        {/* <Grid item xs={12} md={6}>
          <Section title="📦 Meu Novo Componente">
            <MeuComponente />
          </Section>
        </Grid> */}
      </Grid>
    </Box>
  );
};

export default ComponentLab;
