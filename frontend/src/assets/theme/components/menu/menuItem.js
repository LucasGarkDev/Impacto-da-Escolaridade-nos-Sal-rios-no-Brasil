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

// Vision UI Dashboard React base styles
import colors from "assets/theme/base/colors";
import borders from "assets/theme/base/borders";
import typography from "assets/theme/base/typography";

// Vision UI Dashboard React helper functions
import pxToRem from "assets/theme/functions/pxToRem";

const { text, info } = colors;
const { borderRadius } = borders;
const { size, fontWeightMedium } = typography;

export default {
  styleOverrides: {
    root: {
      minWidth: pxToRem(160),
      minHeight: pxToRem(36),
      padding: `${pxToRem(6)} ${pxToRem(18)}`,
      borderRadius: borderRadius.sm,
      fontSize: size.sm,
      fontWeight: fontWeightMedium,
      color: text.main,
      transition: "all 200ms ease",

      "&:hover, &:focus, &.Mui-selected, &.Mui-selected:hover, &.Mui-selected:focus": {
        backgroundColor: info.main,
        color: "#fff",
      },
    },
  },
};

