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

// Vision UI Dashboard React Base Styles
import colors from "assets/theme/base/colors";
import typography from "assets/theme/base/typography";
import boxShadows from "assets/theme/base/boxShadows";
import pxToRem from "assets/theme/functions/pxToRem";

const { white, dark, info, secondary } = colors;
const { size } = typography;
const { buttonBoxShadow } = boxShadows;

export default {
  base: {
    backgroundColor: dark.main,
    minHeight: pxToRem(44),
    color: white.main,
    fontWeight: 600,
    fontSize: size.sm,
    borderRadius: pxToRem(8),
    padding: `${pxToRem(10)} ${pxToRem(22)}`,
    transition: "all 200ms ease-in-out",
    boxShadow: buttonBoxShadow.main,

    "&:hover": {
      backgroundColor: dark.focus,
      transform: "scale(1.03)",
      boxShadow: buttonBoxShadow.stateOf,
    },

    "&:disabled": {
      opacity: 0.5,
      pointerEvents: "none",
    },
  },

  small: {
    minHeight: pxToRem(34),
    fontSize: size.xs,
    padding: `${pxToRem(8)} ${pxToRem(16)}`,
  },

  large: {
    minHeight: pxToRem(56),
    fontSize: size.md,
    padding: `${pxToRem(14)} ${pxToRem(32)}`,
  },

  primary: {
    backgroundColor: info.main,

    "&:hover": {
      backgroundColor: info.focus,
    },
  },

  secondary: {
    backgroundColor: secondary.main,

    "&:hover": {
      backgroundColor: secondary.focus,
    },
  },
};