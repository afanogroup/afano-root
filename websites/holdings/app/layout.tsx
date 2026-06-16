import type { Metadata } from "next";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "AFANO Group Holdings", template: "%s · AFANO Group Holdings" },
  description: "A multinational holding company stewarding 15 Strategic Business Groups across global markets.",
  metadataBase: new URL("https://afanogroup.com"),
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
