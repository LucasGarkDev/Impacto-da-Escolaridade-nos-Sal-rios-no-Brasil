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

import colors from "assets/theme/base/colors";
import typography from "assets/theme/base/typography";
import pxToRem from "assets/theme/functions/pxToRem";

const { info, secondary, dark } = colors;
const { size } = typography;

export default {
  base: {
    color: dark.main,
    border: `${pxToRem(2)} solid ${dark.main}`,
    backgroundColor: "transparent",
    borderRadius: pxToRem(8),
    fontWeight: 500,
    fontSize: size.sm,
    transition: "all 200ms ease",

    "&:hover": {
      backgroundColor: dark.main,
      color: "#fff",
      transform: "translateY(-1px)",
    },
  },

  small: {
    minHeight: pxToRem(34),
    fontSize: size.xs,
    padding: `${pxToRem(6)} ${pxToRem(18)}`,
  },

  large: {
    minHeight: pxToRem(52),
    fontSize: size.md,
    padding: `${pxToRem(12)} ${pxToRem(32)}`,
  },

  primary: {
    borderColor: info.main,
    color: info.main,

    "&:hover": {
      backgroundColor: info.main,
      color: "#fff",
    },
  },

  secondary: {
    borderColor: secondary.main,
    color: secondary.main,

    "&:hover": {
      backgroundColor: secondary.main,
      color: "#fff",
    },
  },
};