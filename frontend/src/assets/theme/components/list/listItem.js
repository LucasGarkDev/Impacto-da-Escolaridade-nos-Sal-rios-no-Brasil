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
import borders from "assets/theme/base/borders";
import pxToRem from "assets/theme/functions/pxToRem";

const { grey } = colors;
const { borderRadius } = borders;

export default {
  defaultProps: {
    disableGutters: true,
  },

  styleOverrides: {
    root: {
      paddingTop: pxToRem(6),
      paddingBottom: pxToRem(6),
      paddingLeft: pxToRem(16),
      paddingRight: pxToRem(16),
      borderRadius: borderRadius.md,
      transition: "background-color 200ms ease, color 200ms ease",

      "&:hover": {
        backgroundColor: grey[200],
      },

      "&.Mui-selected": {
        backgroundColor: grey[300],
        color: grey[900],

        "&:hover": {
          backgroundColor: grey[400],
        },
      },
    },
  },
};

