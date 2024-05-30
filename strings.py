# commands for subprocess
COMMAND_CREATE_APP = ["npm", "create", "vite@latest", "app", "--", "--template", "react-ts"]
COMMAND_MODULES = ["npm", "install"]
COMMAND_SASS = ["npm", "install", "sass", "--save-dev"]

# typeScript file contents
TS_APP_CONTENT = """import "./cssReset.scss";\n
const App = () => {
    return <div>clean cra</div>;
};\n
export default App
"""

TS_INDEX_CONTENT = """import ReactDOM from "react-dom/client";

import App from "./App";

ReactDOM.createRoot(document.getElementById("root")!).render(<App />);
"""

# SCSS content for CSS reset
CSS_RESET_CONTENT = """/* http://meyerweb.com/eric/tools/css/reset/ v2.0 | 20110126 License: none (public domain) */ html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video { margin: 0; padding: 0; border: 0; font-size: 100%; font: inherit; vertical-align: baseline; } /* HTML5 display-role reset for older browsers */ article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section { display: block; } body { line-height: 1; } ol, ul { list-style: none; } blockquote, q { quotes: none; } blockquote:before, blockquote:after, q:before, q:after { content: ""; content: none; } table { border-collapse: collapse; border-spacing: 0; } *, *::before, *::after { box-sizing: border-box; }
"""

TS_TYPE_DECLARATIONS = """declare module "*.png";
declare module "*.svg";
declare module "*.jpeg";
declare module "*.jpg";
declare module "*.scss";
declare module "*.webp";
"""