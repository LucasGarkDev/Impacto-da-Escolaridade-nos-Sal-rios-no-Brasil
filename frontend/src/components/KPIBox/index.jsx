// src/components/KPIBox/index.jsx
import React from "react";
import Card from "@mui/material/Card";
import VuiBox from "components/VuiBox";
import VuiTypography from "components/VuiTypography";
import Icon from "@mui/material/Icon";

const KPIBox = ({ title, value, variation, icon }) => {
  const isPositive = variation && parseFloat(variation) >= 0;

  return (
    <Card
      sx={{
        p: 2,
        height: "100%",
        borderRadius: "12px",
        background: "linear-gradient(135deg, #f0fdf4, #e7f7f5)",
        boxShadow: "0 4px 12px rgba(0,0,0,0.05)",
        transition: "transform 0.15s ease-in-out",
        "&:hover": {
          transform: "translateY(-4px)",
        },
      }}
    >
      <VuiBox display="flex" justifyContent="space-between" alignItems="center">
        <VuiTypography
          variant="subtitle2"
          color="dark"
          fontWeight="bold"
          sx={{ opacity: 0.9, fontSize: "0.95rem", letterSpacing: "0.3px" }}
        >
          {title}
        </VuiTypography>
        {icon && (
          <Icon fontSize="small" color="info" sx={{ opacity: 0.6 }}>
            {icon}
          </Icon>
        )}
      </VuiBox>

      <VuiBox mt={2} display="flex" justifyContent="space-between" alignItems="flex-end">
        <VuiTypography variant="h4" fontWeight="bold" color="dark">
          {value}
        </VuiTypography>
        {variation && (
          <VuiTypography
            variant="caption"
            color={isPositive ? "success" : "error"}
            fontWeight="bold"
          >
            {variation}
          </VuiTypography>
        )}
      </VuiBox>
    </Card>
  );
};

export default KPIBox;


