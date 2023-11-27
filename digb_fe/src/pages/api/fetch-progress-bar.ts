import { backEndAxios } from "@/utils/axios";
import { ProgressBarProps } from "@/pages/index";
import { progressBarEndPoint } from "@/utils/axios/endpoint-config";

const fetchProgressBarData = async (): Promise<ProgressBarProps> => {
  try {
    const { data } = await backEndAxios.get(progressBarEndPoint);
    return data;
  } catch (error) {
    console.error("Error fetching progress bar data:", error);
    throw error;
  }
};

export default fetchProgressBarData;
