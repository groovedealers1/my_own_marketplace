import StuffCard from "./components/StuffCard.jsx";
import ErrorBoundary from "antd/es/alert/ErrorBoundary.js";

function App() {


  return (
      <ErrorBoundary fallback={<p>Something went wrong</p>}>
          <StuffCard/>
      </ErrorBoundary>

  )
}

export default App
