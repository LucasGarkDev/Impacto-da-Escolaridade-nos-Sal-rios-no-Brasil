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

const { primary, grey, text } = colors;
const { size } = typography;

export default {
  base: {
    backgroundColor: "transparent",
    color: primary.main,
    fontWeight: 500,
    padding: `${pxToRem(6)} ${pxToRem(16)}`,
    transition: "all 180ms ease-in-out",

    "&:hover": {
      color: primary.focus,
      backgroundColor: "rgba(0, 0, 0, 0.04)",
    },

    "&:focus": {
      backgroundColor: "rgba(0, 0, 0, 0.06)",
      outline: "none",
    },

    "&:active": {
      opacity: 0.9,
    },

    "&:disabled": {
      color: grey[500],
      cursor: "not-allowed",
    },

    "& .material-icons, .material-icons-round, svg, span": {
      fontSize: pxToRem(16),
    },
  },

  small: {
    fontSize: size.xs,
    padding: `${pxToRem(4)} ${pxToRem(12)}`,
  },

  large: {
    fontSize: size.sm,
    padding: `${pxToRem(10)} ${pxToRem(20)}`,
  },

  primary: {
    color: primary.main,

    "&:hover": {
      color: primary.focus,
    },

    "&:focus": {
      backgroundColor: "rgba(0, 0, 0, 0.04)",
    },
  },

  secondary: {
    color: text.secondary,

    "&:hover": {
      color: text.main,
    },
  },
};