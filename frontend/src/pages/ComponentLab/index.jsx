import React from "react";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import Box from "@mui/material/Box";
import Divider from "@mui/material/Divider";
import VuiTypography from "components/VuiTypography";
import AlertSample from "./samples/AlertSample";
import ProfileInfoCard from "examples/Cards/InfoCards/ProfileInfoCard";


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

        {/* essa e a parte onde voce coloca os componentes que deseja testar */}
        {/* ======================================================================== */}
        <Grid item xs={12} md={6}>
          <Section title="📇 ProfileInfoCard (perfil)">
            <ProfileInfoCard
              title="Usuário"
              description="Descrição fictícia de exemplo"
              info={{
                fullName: "João da Silva",
                mobile: "(11) 99999-9999",
                email: "joao@email.com",
                location: "São Paulo, Brasil",
              }}
              social={[]} // ✅ Adicionado para evitar erro
              action={{ route: "", tooltip: "Editar Perfil" }}
              shadow={false}
            />
          </Section>
        </Grid>
        {/* =============================================================== */}

        
      </Grid>
    </Box>
      
  );
};

export default ComponentLab;
