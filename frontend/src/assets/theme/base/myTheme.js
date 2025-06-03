import { createTheme } from "@mui/material/styles";
import colors from "./base/colors";
import typography from "./base/typography";
import globals from "./base/globals";

const myTheme = createTheme({
  palette: {
    primary: colors.primary,
    secondary: colors.secondary,
    success: colors.success,
    warning: colors.warning,
    error: colors.error,
    info: colors.info,
    background: {
      default: colors.background.default,
    },
    text: {
      primary: colors.text.main,
    },
  },
  typography,
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        body: globals.body,
      },
    },
  },
});

export default myTheme;
