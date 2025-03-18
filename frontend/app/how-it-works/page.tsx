import { Card } from '@/components/ui/card';
import { BarChart2, Package, Truck, Smartphone, QrCode, Database } from 'lucide-react';

export default function HowItWorksPage() {
  const steps = [
    {
      icon: Smartphone,
      title: 'Mobile App Access',
      description: 'Access your inventory management system from anywhere using our mobile-friendly application.',
    },
    {
      icon: QrCode,
      title: 'Scan & Track',
      description: 'Easily scan items into your inventory using QR codes or barcodes for instant tracking.',
    },
    {
      icon: Database,
      title: 'Real-time Updates',
      description: 'All inventory changes are updated in real-time across all connected devices.',
    },
    {
      icon: BarChart2,
      title: 'Analytics Dashboard',
      description: 'Get detailed insights and analytics about your inventory performance.',
    },
    {
      icon: Package,
      title: 'Stock Management',
      description: 'Manage stock levels, set reorder points, and receive low stock alerts automatically.',
    },
    {
      icon: Truck,
      title: 'Supply Chain Integration',
      description: 'Seamlessly integrate with your suppliers and logistics partners.',
    },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-green-50 to-white py-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h1 className="text-4xl font-extrabold text-gray-900 sm:text-5xl sm:tracking-tight lg:text-6xl">
            How BackTrackIt Works
          </h1>
          <p className="mt-5 text-xl text-gray-500 max-w-3xl mx-auto">
            Our smart inventory management system simplifies stock tracking and business operations. Here's how it all comes together.
          </p>
        </div>

        <div className="mt-24">
          <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
            {steps.map((step, index) => {
              const Icon = step.icon;
              return (
                <Card key={index} className="p-8 bg-white border border-gray-200 rounded-2xl shadow-sm hover:shadow-lg transition-shadow duration-300">
                  <div className="flex items-center justify-center w-12 h-12 bg-green-100 rounded-xl mb-6">
                    <Icon className="w-6 h-6 text-green-600" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-4">{step.title}</h3>
                  <p className="text-gray-500">{step.description}</p>
                </Card>
              );
            })}
          </div>

          <div className="mt-24 bg-white rounded-2xl shadow-xl p-8 lg:p-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-8">The Complete Process</h2>
            <div className="relative">
              <div className="border-l-4 border-green-200 ml-6 pl-6 pb-8">
                <div className="flex flex-col space-y-12">
                  <div className="relative">
                    <div className="absolute -left-[3.5rem] bg-green-600 rounded-full w-8 h-8 flex items-center justify-center">
                      <span className="text-white font-semibold">1</span>
                    </div>
                    <h3 className="text-xl font-semibold text-gray-900 mb-2">Initial Setup</h3>
                    <p className="text-gray-500">Get started by setting up your account and customizing your dashboard according to your business needs.</p>
                  </div>
                  <div className="relative">
                    <div className="absolute -left-[3.5rem] bg-green-600 rounded-full w-8 h-8 flex items-center justify-center">
                      <span className="text-white font-semibold">2</span>
                    </div>
                    <h3 className="text-xl font-semibold text-gray-900 mb-2">Import Inventory</h3>
                    <p className="text-gray-500">Import your existing inventory data or start fresh by adding items manually or through bulk upload.</p>
                  </div>
                  <div className="relative">
                    <div className="absolute -left-[3.5rem] bg-green-600 rounded-full w-8 h-8 flex items-center justify-center">
                      <span className="text-white font-semibold">3</span>
                    </div>
                    <h3 className="text-xl font-semibold text-gray-900 mb-2">Daily Operations</h3>
                    <p className="text-gray-500">Track inventory movements, manage stock levels, and generate reports in real-time.</p>
                  </div>
                  <div className="relative">
                    <div className="absolute -left-[3.5rem] bg-green-600 rounded-full w-8 h-8 flex items-center justify-center">
                      <span className="text-white font-semibold">4</span>
                    </div>
                    <h3 className="text-xl font-semibold text-gray-900 mb-2">Analyze & Optimize</h3>
                    <p className="text-gray-500">Use our advanced analytics to make data-driven decisions and optimize your inventory management.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}