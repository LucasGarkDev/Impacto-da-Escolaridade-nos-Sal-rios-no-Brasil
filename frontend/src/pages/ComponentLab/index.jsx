import React from "react";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import Box from "@mui/material/Box";
import Divider from "@mui/material/Divider";
import VuiTypography from "components/VuiTypography";
import colors from "assets/theme/base/colors";

// Importação dos componentes personalizados
// import VuiAlert from "components/VuiAlert";
// import VuiAvatar from "components/VuiAvatar";
// import VuiBadge from "components/VuiBadge";
// import VuiBox from "components/VuiBox";
// import VuiButton from "components/VuiButton";
// import VuiInput from "components/VuiInput";
// import VuiPagination from "components/VuiPagination";
// import VuiProgress from "components/VuiProgress";
// import VuiSwitch from "components/VuiSwitch";


// Exemplos (do dashboard)
// import ProfileInfoCard from "examples/Cards/InfoCards/ProfileInfoCard";
// import MiniStatisticsCard from "examples/Cards/StatisticsCards/MiniStatisticsCard";
//  // ajuste se for diferente
// import MasterCard from "examples/Cards/MasterCard";
// import BarChart from "examples/Charts/BarCharts/BarChart"; // exemplo base, substitua conforme os nomes reais
// import LineChart from "examples/Charts/LineCharts/LineChart";

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

          <Grid item xs={12}>
      <Section title="🎓 Escolaridade - Cores Oficiais">
        <Grid container spacing={2}>
          {Object.entries(colors.custom.escolaridade).map(([nivel, cor]) => (
            <Grid item xs={12} sm={6} md={4} key={nivel}>
              <Box
                sx={{
                  backgroundColor: cor,
                  color: "#fff",
                  p: 2,
                  borderRadius: "8px",
                  boxShadow: 2,
                  textTransform: "capitalize",
                }}
              >
                {nivel}
              </Box>
            </Grid>
          ))}
        </Grid>
      </Section>
    </Grid>
    </Box>
  );
};

export default ComponentLab;