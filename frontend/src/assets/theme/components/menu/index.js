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
import boxShadows from "assets/theme/base/boxShadows";
import typography from "assets/theme/base/typography";
import colors from "assets/theme/base/colors";
import borders from "assets/theme/base/borders";
// import linearGradient from "assets/theme/functions/linearGradient";

// Vision UI Dashboard React helper functions
import pxToRem from "assets/theme/functions/pxToRem";

const { borderWidth, borderRadius } = borders;
const { lg } = boxShadows;
const { size } = typography;
const { text, white, gradients, grey, custom } = colors;

export default {
  defaultProps: {
    disableAutoFocusItem: true,
  },

  styleOverrides: {
    "& .MuiIcon-root": {
      stroke: text.main,
    },

    paper: {
      minWidth: pxToRem(180),
      boxShadow: lg,
      padding: 0,
      fontSize: size.sm,
      color: text.main,
      background: white.main,
      textAlign: "left",
      border: `${borderWidth[1]} solid ${grey[300]}`,
      borderRadius: borderRadius.md,
    },

    list: {
      background: white.main,

      "& .MuiMenuItem-root": {
        "& .MuiBox-root .MuiTypography-root": {
          color: text.main,
        },
        "&:hover": {
          backgroundColor: grey[200],
        },
        "&.Mui-selected, &.Mui-selected:hover": {
          backgroundColor: custom.light || gradients.info.main,
          color: white.main,
        },
      },
    },
  },
};
