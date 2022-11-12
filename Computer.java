public class Computer{
	private String brand;
	private String model;
	private String year;
	private String serialNumber;
	private String OS;
	private String OSVersion;
	private String screenResolution;
	private double screenSize;
	private int memory;
	private int storage;
	private int CPUCoreCount;
	private int GPUCoreCount;

	public Computer(String brand, String model, String year){
		this.brand = brand;
		this.model = model;
		this.year = year;
	}

	public Computer(String brand, String year, String OS, String screenResolution){
		this.brand = brand;
		this.year = year;
		this.OS = OS;
		this.screenResolution = screenResolution;
	}

	public Computer(String brand, String model, String year, String serialNumber, String OS, String OSVersion, String screenResolution, double screenSize, int memory, int storage, int CPUCoreCount, int GPUCoreCount){
		this.brand = brand;
		this.model = model;
		this.year = year;
		this.serialNumber = serialNumber;
		this.OS = OS;
		this.OSVersion = OSVersion;
		this.screenResolution = screenResolution;
		this.screenSize = screenSize;
		this.memory = memory;
		this.storage = storage;
		this.CPUCoreCount = CPUCoreCount;
		this.GPUCoreCount = GPUCoreCount;
	}

	public Computer(){}

	public void setBrand(String brand){
		this.brand = brand;
	}

	public String getBrand(){
		return this.brand;
	}

	public void setModel(String model){
		this.model = model;
	}

	public String getModel(){
		return this.model;
	}

	public void setYear(String year){
		this.year = year;
	}

	public String getYear(){
		return this.year;
	}

	public void setSerialNumber(String serialNumber){
		this.serialNumber = serialNumber;
	}

	public String getSerialNumber(){
		return this.serialNumber;
	}

	public void setOS(String OS){
		this.OS = OS;
	}

	public String getOS(){
		return this.OS;
	}

	public void setOSVersion(String OSVersion){
		this.OSVersion = OSVersion;
	}

	public String getOSVersion(){
		return this.OSVersion;
	}

	public void setScreenResolution(String screenResolution){
		this.screenResolution = screenResolution;
	}

	public String getScreenResolution(){
		return this.screenResolution;
	}

	public void setScreenSize(double screenSize){
		this.screenSize = screenSize;
	}

	public double getScreenSize(){
		return this.screenSize;
	}

	public void setMemory(int memory){
		this.memory = memory;
	}

	public int getMemory(){
		return this.memory;
	}

	public void setStorage(int storage){
		this.storage = storage;
	}

	public int getStorage(){
		return this.storage;
	}

	public void setCPUCoreCount(int CPUCoreCount){
		this.CPUCoreCount = CPUCoreCount;
	}

	public int getCPUCoreCount(){
		return this.CPUCoreCount;
	}

	public void setGPUCoreCount(int GPUCoreCount){
		this.GPUCoreCount = GPUCoreCount;
	}

	public int getGPUCoreCount(){
		return this.GPUCoreCount;
	}
}
