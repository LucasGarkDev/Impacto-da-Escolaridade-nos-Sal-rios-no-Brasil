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

import borders from "assets/theme/base/borders";
import pxToRem from "assets/theme/functions/pxToRem";

const { borderRadius } = borders;

export default {
  styleOverrides: {
    root: {
      borderRadius: borderRadius.lg, // um pouco menor para combinar com `card`
      margin: `${pxToRem(16)} ${pxToRem(16)} 0`,
      overflow: "hidden", // evita imagens saindo da borda
    },

    media: {
      width: "100%",
      objectFit: "cover", // garante proporção mais bonita
      display: "block",
    },
  },
};
