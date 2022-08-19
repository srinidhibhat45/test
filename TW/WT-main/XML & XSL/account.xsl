<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/bank">
    <html>
        <body>
            <h2>Account List</h2>

            <table border="1">
                <tr style="background-color:green">
                    <th>Account Number</th>
                    <th>Account Type</th>
                    <th>Name</th>
                    <th>Balance</th>
                </tr>

                <xsl:for-each select="account">
                    <tr>
                        <td><xsl:value-of select="acc_no"/></td>
                        <td><xsl:value-of select="acc_type"/></td>
                        <td><xsl:value-of select="name"/></td>
                        <td><xsl:value-of select="balance"/></td>
                    </tr>   
                </xsl:for-each>
            </table>    
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>