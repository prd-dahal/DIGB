import { useState, useEffect } from "react";
import { ProgressBarProps } from "@/pages";

const ProgressBar: React.FC<ProgressBarProps> = ({ progressBarData }) => {
  const [currentStep, setCurrentStep] = useState(0);

  const handleNext = () => {
    setCurrentStep((prevStep) =>
      prevStep < progressBarData.length - 1 ? prevStep + 1 : prevStep
    );
  };

  const handlePrev = () => {
    setCurrentStep((prevStep) => (prevStep > 0 ? prevStep - 1 : prevStep));
  };

  const currentItem = progressBarData[currentStep];

  const progressPercentage = ((currentStep + 1) / progressBarData.length) * 100;

  const progressBarColor =
    progressPercentage < 25
      ? "bg-red-500"
      : progressPercentage < 50
      ? "bg-yellow-500"
      : progressPercentage < 75
      ? "bg-blue-500"
      : "bg-green-500";

  // Animation Effect
  useEffect(() => {
    const progressBar = document.getElementById("progress-bar");
    if (progressBar) {
      progressBar.style.width = `${progressPercentage}%`;
      progressBar.className = `h-full ${progressBarColor} transition-width duration-500 ease-in-out`;
    }
  }, [progressPercentage, progressBarColor]);

  return (
    <div className="w-full max-w-3xl mx-auto p-4">
      <div className="mb-4 flex justify-between items-center">
        <div className="flex flex-wrap">
          {progressBarData.map((step, index) => (
            <div key={index} className="flex-shrink-0">
              <span
                className={`${
                  index <= currentStep
                    ? "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-teal-600 bg-teal-200"
                    : "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-500 bg-gray-200"
                }`}
              >
                {step.title}
              </span>
            </div>
          ))}
        </div>
      </div>
      <div className="relative">
        <div className="h-4 bg-gray-200 rounded-full overflow-hidden">
          <div
            id="progress-bar"
            className={`h-full ${progressBarColor} transition-width duration-500 ease-in-out`}
          >
            <div className="flex justify-center align-center text-[12px] h-[16px] z-2">
              <span className=" text-white">{`${progressPercentage.toFixed(
                2
              )}%`}</span>
            </div>
          </div>
        </div>
      </div>
      <div className="mb-4 mt-4">
        <h2 className="text-2xl font-bold">{currentItem.title}</h2>
        <p className="text-gray-600 mt-1">{currentItem.subtitle}</p>
      </div>
      <div
        className="mb-4"
        dangerouslySetInnerHTML={{ __html: currentItem.content }}
      ></div>
      <div className="flex justify-between">
        <button
          onClick={handlePrev}
          className="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition-all duration-300"
        >
          Previous
        </button>
        <button
          onClick={handleNext}
          className="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition-all duration-300"
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default ProgressBar;
