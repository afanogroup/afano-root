import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "AFANO Tourism, Hospitality & Mobility Group", template: "%s · AFANO Tourism, Hospitality & Mobility Group" },
  description: "An independent operating subsidiary within AFANO Group Holdings.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
