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

function navbar(theme, ownerState) {
  const { palette, boxShadows, functions, transitions, breakpoints, borders } = theme;
  const { transparentNavbar, absolute, light } = ownerState;

  const { dark, text, transparent, gradients, borderCol } = palette;
  const { navbarBoxShadow } = boxShadows;
  const { linearGradient, pxToRem } = functions;
  const { borderRadius } = borders;

  return {
    boxShadow: transparentNavbar || absolute ? "none" : navbarBoxShadow,
    backdropFilter: transparentNavbar || absolute ? "none" : `blur(${pxToRem(42)})`,
    backgroundColor: `${transparent.main} !important`,
    backgroundImage:
      transparentNavbar || absolute
        ? `none`
        : `${linearGradient(
            gradients.navbar.main,
            gradients.navbar.state,
            gradients.navbar.deg
          )} !importants`,

    color: () => {
      if (light) return text.main;
      if (transparentNavbar) return text.main;
      return dark.main;
    },
    top: absolute ? 0 : pxToRem(12),
    minHeight: pxToRem(75),
    display: "grid",
    alignItems: "center",

    borderRadius: borderRadius.xl,
    borderColor:
      transparentNavbar || absolute
        ? `${transparent.main} !important`
        : `${borderCol.navbar} !important`,
    paddingTop: pxToRem(8),
    paddingBottom: pxToRem(8),
    paddingRight: absolute ? pxToRem(8) : 0,
    paddingLeft: absolute ? pxToRem(16) : 0,

    "& > *": {
      transition: transitions.create("all", {
        easing: transitions.easing.easeInOut,
        duration: transitions.duration.standard,
      }),
    },

    "& .MuiToolbar-root": {
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",

      [breakpoints.up("sm")]: {
        minHeight: "auto",
        padding: `${pxToRem(4)} ${pxToRem(16)}`,
      },
    },
  };
}

const navbarContainer = ({ breakpoints }) => ({
  flexDirection: "column",
  alignItems: "flex-start",
  justifyContent: "space-between",
  pt: 0.5,
  pb: 0.5,

  [breakpoints.up("md")]: {
    flexDirection: "row",
    alignItems: "center",
    paddingTop: "0",
    paddingBottom: "0",
  },
});

const navbarRow = ({ breakpoints, palette: { white, text } }, { isMini, light }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "space-between",
  width: "100%",
  "&.MuiBox-root": {
    "& nav": {
      "& ol": {
        "& li": {
          "&.MuiBreadcrumbs-li": {
            "& a": {
              "& span": {
                color: light ? text.main : white.main,
              },
            },
          },
          "&.MuiBreadcrumbs-li span.MuiTypography-button": {
            color: light ? text.main : white.main,
          },
          "&.MuiBreadcrumbs-separator": {
            color: light ? text.main : white.main,
          },
        },
      },
    },
  },
  "& h6": {
    color: "rgb(31, 29, 29)",
  },

  [breakpoints.up("md")]: {
    justifyContent: isMini ? "space-between" : "stretch",
    width: isMini ? "100%" : "max-content",
  },

  [breakpoints.up("xl")]: {
    justifyContent: "stretch !important",
    width: "max-content !important",
  },
});

const navbarIconButton = (theme) => {
  const { typography: { size }, breakpoints, palette: { white, text } } = theme;
  const light = theme.ownerState?.light; // 🔍 tenta buscar da ownerState

  return {
    px: 0.75,
    "& .material-icons, .material-icons-round": {
      fontSize: `${size.md} !important`,
      color: light ? text.main : white.main,
    },
    "& .MuiTypography-root": {
      display: "none",
      color: light ? text.main : white.main,

      [breakpoints.up("sm")]: {
        display: "inline-block",
        lineHeight: 1.2,
        ml: 0.5,
      },
    },
  };
};

const navbarMobileMenu = (theme) => {
  const { breakpoints, palette: { white, text } } = theme;
  const light = theme.ownerState?.light;

  return {
    display: "inline-block",
    lineHeight: 0,
    color: light ? text.main : white.main,

    [breakpoints.up("xl")]: {
      display: "none",
    },
  };
};


export { navbar, navbarContainer, navbarRow, navbarIconButton, navbarMobileMenu };
