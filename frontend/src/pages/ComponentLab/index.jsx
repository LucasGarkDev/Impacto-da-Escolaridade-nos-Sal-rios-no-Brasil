import React from "react";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import Box from "@mui/material/Box";
import Divider from "@mui/material/Divider";
import VuiTypography from "components/VuiTypography";

import KPIBox from "components/KPIBox"; // ✅ direto do componente real


// Wrapper para seções de testes
const Section = ({ title, children }) => (
  <Card sx={{ p: 3, mb: 4 }}>
    <VuiTypography variant="h6" gutterBottom>
      {title}
    </VuiTypography>
    <Divider sx={{ mb: 2 }} />
    {children}
  </Card>
);

const ComponentLab = () => {
  return (
    <Box p={3}>
      <VuiTypography variant="h4" mb={4}>
        🔬 Component Lab Completo
      </VuiTypography>

      <Section title="💠 Teste direto do KPIBox">
        <Grid container spacing={2}>
          <Grid item xs={12} md={4}>
            <KPIBox title="Total de Registros" value="53.000" variation="+5%" icon="assessment" />
          </Grid>
          <Grid item xs={12} md={4}>
            <KPIBox title="% com Renda Zero" value="27%" variation="-2%" icon="person_off" />
          </Grid>
          <Grid item xs={12} md={4}>
            <KPIBox title="Renda Média (Sexo)" value="R$ 2.814" variation="+1.2%" icon="groups" />
          </Grid>
        </Grid>
      </Section>
    </Box>
  );
};

export default ComponentLab;