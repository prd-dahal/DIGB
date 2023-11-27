import React from "react";
import fetchProgressBarData from "@/pages/api/fetch-progress-bar";
import ProgressBar from "@/components/ProgressBar";
export interface ProgressBarItem {
  title: string;
  subtitle: string;
  order: number;
  content: string;
}

export interface ProgressBarProps {
  progressBarData: ProgressBarItem[];
}

const Home: React.FC<ProgressBarProps> = ({ progressBarData }) => {
  return <ProgressBar progressBarData={progressBarData} />;
};

export async function getStaticProps() {
  try {
    // Fetch data from the API
    const progressBarData = await fetchProgressBarData();
    return {
      props: {
        progressBarData,
      },
      // Incremental Static Regeneration (ISR) configuration
      revalidate: 60, // In seconds. This means the page will be re-generated every 60 seconds if a request comes in.
    };
  } catch (error) {
    console.error("Error fetching data:", error);
    return {
      props: {
        progressBarData: null,
      },
    };
  }
}
export default Home;
