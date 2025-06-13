/*!

=========================================================
* Vision UI Free React - v1.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/vision-ui-free-react
* Copyright 2021 Creative Tim (https://www.creative-tim.com/)
* Licensed under MIT (https://github.com/creativetimofficial/vision-ui-free-react/blob/master LICENSE.md)

* Design and Coded by Simmmple & Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/

// @mui material components
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";
import { Card, LinearProgress, Stack } from "@mui/material";

// Vision UI Dashboard React components
import VuiBox from "components/VuiBox";
import VuiTypography from "components/VuiTypography";
import VuiProgress from "components/VuiProgress";

// Vision UI Dashboard React example components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";
import MiniStatisticsCard from "examples/Cards/StatisticsCards/MiniStatisticsCard";
// import linearGradient from "assets/theme/functions/linearGradient";

// Vision UI Dashboard React base styles
// import typography from "assets/theme/base/typography";
// import colors from "assets/theme/base/colors";

// Dashboard layout components
import WelcomeMark from "layouts/dashboard/components/WelcomeMark";
import Projects from "layouts/dashboard/components/Projects";
import OrderOverview from "layouts/dashboard/components/OrderOverview";
import SatisfactionRate from "layouts/dashboard/components/SatisfactionRate";
import ReferralTracking from "layouts/dashboard/components/ReferralTracking";

// React icons
import { IoIosRocket } from "react-icons/io";
import { IoGlobe } from "react-icons/io5";
import { IoBuild } from "react-icons/io5";
import { IoWallet } from "react-icons/io5";
import { IoDocumentText } from "react-icons/io5";
import { FaShoppingCart } from "react-icons/fa";



// Data
import LineChart from "examples/Charts/LineCharts/LineChart.jsx";
import BarChart from "examples/Charts/BarCharts/BarChart.jsx";
// import { lineChartDataDashboard } from "layouts/dashboard/data/lineChartData";
// import { lineChartOptionsDashboard } from "layouts/dashboard/data/lineChartOptions";
// import { barChartDataDashboard } from "layouts/dashboard/data/barChartData";
// import { barChartOptionsDashboard } from "layouts/dashboard/data/barChartOptions";

import KPIBox from "components/KPIBox";
import TotalRegistrosIcon from "assets/images/icones/KPIBox/total-registros.svg?react";
import PorcentagemRendaZero from "assets/images/icones/KPIBox/porcentagem-renda-zero.svg?react";


function Dashboard() {
  // const { gradients } = colors;
  // const { cardContent } = gradients;

  return (
    <DashboardLayout>
      <DashboardNavbar />
      
      <VuiBox py={3}>
      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <KPIBox
            title="Total de Registros"
            value="53.000"
            variation="+5%"
            icon={<TotalRegistrosIcon width={36} height={36} />}
          />
        </Grid>
        <Grid item xs={12} md={4}>
          <KPIBox
            title="% com Renda Zero"
            value="27%"
            variation="-2%"
            icon={<PorcentagemRendaZero width={36} height={36}/>}
          />
        </Grid>
      </Grid>
    </VuiBox>



      <Footer />
    </DashboardLayout>
  );
}

export default Dashboard;
