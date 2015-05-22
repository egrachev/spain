<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/pages">
    <html>
    <head>
        <style type="text/css">
            body {
                font-size:0.83em;
            }
        </style>
    </head>
    <body>
        <h1>Карта сайта</h1>
        <ul>

            <xsl:for-each select="page">
                <li>
                    <xsl:element name="a">
                        <xsl:attribute name="href">
                            <xsl:value-of select="url"/>
                        </xsl:attribute>
                        <xsl:value-of select="title"/>
                    </xsl:element>
                </li>
            </xsl:for-each>

        </ul>
    </body>
    </html>
</xsl:template>
</xsl:stylesheet>