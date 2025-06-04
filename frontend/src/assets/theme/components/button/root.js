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

import typography from "assets/theme/base/typography";
import borders from "assets/theme/base/borders";
import pxToRem from "assets/theme/functions/pxToRem";

const { fontWeightSemiBold, size } = typography;
const { borderRadius } = borders;

export default {
  display: "inline-flex",
  justifyContent: "center",
  alignItems: "center",
  fontSize: size.sm,
  fontWeight: fontWeightSemiBold, // Mais elegante e legível
  borderRadius: borderRadius.md,
  padding: `${pxToRem(10)} ${pxToRem(20)}`,
  lineHeight: 1.4,
  textAlign: "center",
  textTransform: "capitalize",
  userSelect: "none",
  cursor: "pointer",
  backgroundSize: "120%",
  backgroundPosition: "center",
  transition: "all 200ms ease",

  "&:hover": {
    transform: "scale(1.015)",
    filter: "brightness(1.03)",
  },

  "&:disabled": {
    pointerEvents: "none",
    opacity: 0.5,
  },

  "& .material-icons": {
    fontSize: pxToRem(18),
    marginTop: pxToRem(-2),
  },
};