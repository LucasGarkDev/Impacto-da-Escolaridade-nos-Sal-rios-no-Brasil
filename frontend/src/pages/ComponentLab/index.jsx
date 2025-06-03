import React from "react";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import Box from "@mui/material/Box";
import Divider from "@mui/material/Divider";
import VuiTypography from "components/VuiTypography";
// Importação dos componentes personalizados
import VuiAlert from "components/VuiAlert";
import VuiAvatar from "components/VuiAvatar";
import VuiBadge from "components/VuiBadge";
import VuiBox from "components/VuiBox";
import VuiButton from "components/VuiButton";
import VuiInput from "components/VuiInput";
import VuiPagination from "components/VuiPagination";
import VuiProgress from "components/VuiProgress";
import VuiSwitch from "components/VuiSwitch";

// Exemplos (do dashboard)
import ProfileInfoCard from "examples/Cards/InfoCards/ProfileInfoCard";
import MiniStatisticsCard from "examples/Cards/StatisticsCards/MiniStatisticsCard";
 // ajuste se for diferente
import MasterCard from "examples/Cards/MasterCard";
import BarChart from "examples/Charts/BarCharts/BarChart"; // exemplo base, substitua conforme os nomes reais
import LineChart from "examples/Charts/LineCharts/LineChart";

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

      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Section title="🧪 VuiAlert">
            <VuiAlert color="success">Sucesso!</VuiAlert>
          </Section>
        </Grid>

        <Grid item xs={12} md={6}>
          <Section title="👤 VuiAvatar">
            <VuiAvatar src="assets/images/avatar1.png" alt="avatar" />
          </Section>
        </Grid>

        <Grid item xs={12} md={6}>
          <Section title="📛 VuiBadge">
            <VuiBadge color="error" content="5" />
          </Section>
        </Grid>

        <Grid item xs={12} md={6}>
          <Section title="📦 VuiBox">
            <VuiBox p={2} bgColor="primary" color="white">Box com fundo</VuiBox>
          </Section>
        </Grid>

        <Grid item xs={12} md={6}>
          <Section title="🟣 VuiButton">
            <VuiButton color="info">Clique Aqui</VuiButton>
          </Section>
        </Grid>

        <Grid item xs={12} md={6}>
          <Section title="✏️ VuiInput">
            <VuiInput placeholder="Digite algo..." />
          </Section>
        </Grid>

        <Grid item xs={12} md={6}>
          <Section title="📄 VuiPagination">
            <VuiPagination count={5} />
          </Section>
        </Grid>

        <Grid item xs={12} md={6}>
          <Section title="📊 VuiProgress">
            <VuiProgress value={60} />
          </Section>
        </Grid>

        <Grid item xs={12} md={6}>
          <Section title="🔘 VuiSwitch">
            <VuiSwitch checked />
          </Section>
        </Grid>

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
              social={[]} // necessário!
              action={{ route: "", tooltip: "Editar Perfil" }}
              shadow={false}
            />
          </Section>
        </Grid>

        <Grid item xs={12} md={4}>
          <Section title="📊 MiniStatisticsCard">
            <MiniStatisticsCard
              title={{ text: "Usuários" }}
              count="1.250"
              percentage={{ color: "success", text: "+5%" }}
              icon={{ color: "info", component: "group" }}
            />
          </Section>
        </Grid>

        <Grid item xs={12} md={6}>
          <Section title="💳 MasterCard">
            <MasterCard
              number="1234 5678 9012 3456"
              holder="JOÃO SILVA"
              expires="12/25"
            />
          </Section>
        </Grid>

        <Grid item xs={12}>
          <Section title="📉 LineChart (Fluxo)">
            <LineChart
              title="Tráfego"
              chart={{
                labels: ["Seg", "Ter", "Qua", "Qui", "Sex"],
                datasets: [
                  {
                    label: "Visitantes",
                    color: "info",
                    data: [50, 120, 70, 180, 200],
                  },
                ],
              }}
            />
          </Section>
        </Grid>

        <Grid item xs={12}>
          <Section title="📈 BarChart (Exemplo)">
            <BarChart
              title="Vendas Mensais"
              chart={{
                labels: ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
                datasets: [
                  {
                    label: "Vendas",
                    backgroundColor: "#4c51bf",
                    data: [450, 200, 100, 220, 500, 1000],
                  },
                ],
              }}
            />
          </Section>
        </Grid>


      </Grid>
    </Box>
  );
};

export default ComponentLab;